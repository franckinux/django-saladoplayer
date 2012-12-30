# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tour'
        db.create_table('saladoplayer_tour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('dropmenu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('viewfinder', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('scrollmenu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gallery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('zoomslider', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('auto_rotation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('full_screener', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('compass', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('facebook', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumb', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='thumb', null=True, to=orm['photologue.Photo'])),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=600)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=800)),
            ('first_panorama', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='first_panorama', null=True, to=orm['saladoplayer.Panorama'])),
            ('photo_size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.PhotoSize'], null=True, blank=True)),
            ('nadir', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nadir', null=True, to=orm['photologue.Photo'])),
        ))
        db.send_create_signal('saladoplayer', ['Tour'])

        # Adding model 'Panorama'
        db.create_table('saladoplayer_panorama', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tour', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saladoplayer.Tour'])),
            ('directory', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('initial_pan', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('initial_tilt', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('min_tilt', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('max_tilt', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.Gallery'], null=True, blank=True)),
            ('direction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('saladoplayer', ['Panorama'])

        # Adding model 'PanoramaHotspot'
        db.create_table('saladoplayer_panoramahotspot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_panorama', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_pano', to=orm['saladoplayer.Panorama'])),
            ('to_panorama', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_pano', to=orm['saladoplayer.Panorama'])),
            ('show_information', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pan', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('tilt', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('saladoplayer', ['PanoramaHotspot'])

        # Adding unique constraint on 'PanoramaHotspot', fields ['from_panorama', 'to_panorama']
        db.create_unique('saladoplayer_panoramahotspot', ['from_panorama_id', 'to_panorama_id'])

        # Adding model 'Map'
        db.create_table('saladoplayer_map', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('map_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.Photo'])),
            ('tour', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saladoplayer.Tour'])),
            ('pan_shift', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('saladoplayer', ['Map'])

        # Adding model 'PanoramaMapping'
        db.create_table('saladoplayer_panoramamapping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saladoplayer.Map'])),
            ('panorama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saladoplayer.Panorama'])),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('saladoplayer', ['PanoramaMapping'])

        # Adding model 'InformationHotspot'
        db.create_table('saladoplayer_informationhotspot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('panorama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saladoplayer.Panorama'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('pan', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('tilt', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('saladoplayer', ['InformationHotspot'])

        # Adding model 'LinkHotspot'
        db.create_table('saladoplayer_linkhotspot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('panorama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saladoplayer.Panorama'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('pan', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('tilt', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('saladoplayer', ['LinkHotspot'])


    def backwards(self, orm):
        # Removing unique constraint on 'PanoramaHotspot', fields ['from_panorama', 'to_panorama']
        db.delete_unique('saladoplayer_panoramahotspot', ['from_panorama_id', 'to_panorama_id'])

        # Deleting model 'Tour'
        db.delete_table('saladoplayer_tour')

        # Deleting model 'Panorama'
        db.delete_table('saladoplayer_panorama')

        # Deleting model 'PanoramaHotspot'
        db.delete_table('saladoplayer_panoramahotspot')

        # Deleting model 'Map'
        db.delete_table('saladoplayer_map')

        # Deleting model 'PanoramaMapping'
        db.delete_table('saladoplayer_panoramamapping')

        # Deleting model 'InformationHotspot'
        db.delete_table('saladoplayer_informationhotspot')

        # Deleting model 'LinkHotspot'
        db.delete_table('saladoplayer_linkhotspot')


    models = {
        'photologue.gallery': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Gallery'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photologue.Photo']"}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'photologue.photosize': {
            'Meta': {'ordering': "['width', 'height']", 'object_name': 'PhotoSize'},
            'crop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'increment_count': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'pre_cache': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quality': ('django.db.models.fields.PositiveIntegerField', [], {'default': '70'}),
            'upscale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'watermark': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': "orm['photologue.Watermark']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.watermark': {
            'Meta': {'object_name': 'Watermark'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'opacity': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'scale'", 'max_length': '5'})
        },
        'saladoplayer.informationhotspot': {
            'Meta': {'object_name': 'InformationHotspot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pan': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'panorama': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['saladoplayer.Panorama']"}),
            'tilt': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'saladoplayer.linkhotspot': {
            'Meta': {'object_name': 'LinkHotspot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pan': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'panorama': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['saladoplayer.Panorama']"}),
            'tilt': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'saladoplayer.map': {
            'Meta': {'object_name': 'Map'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Photo']"}),
            'pan_shift': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['saladoplayer.Tour']"})
        },
        'saladoplayer.panorama': {
            'Meta': {'object_name': 'Panorama'},
            'chaining': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['saladoplayer.Panorama']", 'through': "orm['saladoplayer.PanoramaHotspot']", 'symmetrical': 'False'}),
            'direction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'directory': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Gallery']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_pan': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'initial_tilt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'max_tilt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'min_tilt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['saladoplayer.Tour']"})
        },
        'saladoplayer.panoramahotspot': {
            'Meta': {'unique_together': "(('from_panorama', 'to_panorama'),)", 'object_name': 'PanoramaHotspot'},
            'from_panorama': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_pano'", 'to': "orm['saladoplayer.Panorama']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pan': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'show_information': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tilt': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'to_panorama': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_pano'", 'to': "orm['saladoplayer.Panorama']"})
        },
        'saladoplayer.panoramamapping': {
            'Meta': {'object_name': 'PanoramaMapping'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['saladoplayer.Map']"}),
            'panorama': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['saladoplayer.Panorama']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        'saladoplayer.tour': {
            'Meta': {'object_name': 'Tour'},
            'auto_rotation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'compass': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dropmenu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_panorama': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'first_panorama'", 'null': 'True', 'to': "orm['saladoplayer.Panorama']"}),
            'full_screener': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '600'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nadir': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nadir'", 'null': 'True', 'to': "orm['photologue.Photo']"}),
            'photo_size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.PhotoSize']", 'null': 'True', 'blank': 'True'}),
            'scrollmenu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thumb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'thumb'", 'null': 'True', 'to': "orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'viewfinder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '800'}),
            'zoomslider': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['saladoplayer']