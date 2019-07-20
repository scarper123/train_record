/**
 * 
 * @authors Shanming (shanming0428@163.com)
 * @date    2019-07-12 23:21:43
 * @version $Id$
 */

import React from 'react';
import {
    List,
    Datagrid,
    TextField,
    EmailField,
    UrlField,
    BooleanField,
    ReferenceField,
    Edit,
    SimpleForm,
    DisabledInput,
    ReferenceInput,
    SelectInput,
    TextInput,
    LongTextInput,
    Create,
    BooleanInput,
    EditButton,
    Responsive,
    SimpleList
} from 'react-admin';
import MyUrlField from './MyUrlField';
import RichTextInput from 'ra-input-rich-text';


export const CourseList = props => (
    <List {...props}>
        <Responsive 
        small={
            <SimpleList
                primaryText={user => user.name}
                secondaryText={user => user.email}
                />
        }
        medium={
            <Datagrid>
                <TextField source="id" />
                <TextField source="name" />
                <TextField source="tel" />
                <TextField source="website" />
                <TextField source="desc" />
                <EditButton />
            </Datagrid>
        } />
    </List>
)

export const CourseEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <DisabledInput source="id" />
            <TextInput source="name" />
            <TextInput source="tel" />
            <TextInput source="website" />
            <RichTextInput source="desc" />
        </SimpleForm>
    </Edit>
);

export const CourseCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <TextInput source="tel" />
            <TextInput source="website" />
            <RichTextInput source="desc" />
        </SimpleForm>
    </Create>
);