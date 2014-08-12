# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Platform'
        db.create_table(u'core_platform', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'core', ['Platform'])

        # Adding model 'Developer'
        db.create_table(u'core_developer', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'core', ['Developer'])

        # Adding model 'Library'
        db.create_table(u'core_library', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Platform'])),
            ('link', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'core', ['Library'])

        # Adding unique constraint on 'Library', fields ['name', 'platform']
        db.create_unique(u'core_library', ['name', 'platform_id'])

        # Adding model 'LibraryVersion'
        db.create_table(u'core_libraryversion', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('library', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Library'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['LibraryVersion'])

        # Adding unique constraint on 'LibraryVersion', fields ['library', 'version']
        db.create_unique(u'core_libraryversion', ['library_id', 'version'])

        # Adding model 'Project'
        db.create_table(u'core_project', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'core', ['Project'])

        # Adding model 'Post'
        db.create_table(u'core_post', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('library', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.LibraryVersion'])),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Developer'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Project'])),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Post'])

        # Adding unique constraint on 'Post', fields ['library', 'project', 'developer']
        db.create_unique(u'core_post', ['library_id', 'project_id', 'developer_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Post', fields ['library', 'project', 'developer']
        db.delete_unique(u'core_post', ['library_id', 'project_id', 'developer_id'])

        # Removing unique constraint on 'LibraryVersion', fields ['library', 'version']
        db.delete_unique(u'core_libraryversion', ['library_id', 'version'])

        # Removing unique constraint on 'Library', fields ['name', 'platform']
        db.delete_unique(u'core_library', ['name', 'platform_id'])

        # Deleting model 'Platform'
        db.delete_table(u'core_platform')

        # Deleting model 'Developer'
        db.delete_table(u'core_developer')

        # Deleting model 'Library'
        db.delete_table(u'core_library')

        # Deleting model 'LibraryVersion'
        db.delete_table(u'core_libraryversion')

        # Deleting model 'Project'
        db.delete_table(u'core_project')

        # Deleting model 'Post'
        db.delete_table(u'core_post')


    models = {
        u'core.developer': {
            'Meta': {'object_name': 'Developer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'core.library': {
            'Meta': {'unique_together': "(('name', 'platform'),)", 'object_name': 'Library'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Platform']"})
        },
        u'core.libraryversion': {
            'Meta': {'unique_together': "(('library', 'version'),)", 'object_name': 'LibraryVersion'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'library': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Library']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.platform': {
            'Meta': {'object_name': 'Platform'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'core.post': {
            'Meta': {'unique_together': "(('library', 'project', 'developer'),)", 'object_name': 'Post'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Developer']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'library': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.LibraryVersion']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Project']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['core']