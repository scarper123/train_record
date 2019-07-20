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
    SimpleList,
    NumberField,
    NumberInput
} from 'react-admin';
import MyUrlField from './MyUrlField';
import RichTextInput from 'ra-input-rich-text';


export const RoleList = props => (
    <List {...props}>
        <Responsive 
        small={
            <SimpleList
                primaryText={role => role.name}
                secondaryText={role => role.permissions}
                tertiaryText={role => role.desc}
                />
        }
        medium={
            <Datagrid>
                <TextField source="id" />
                <TextField source="name" />
                <NumberField source="permissions" />
                <TextField source="desc" />
                <EditButton />
            </Datagrid>
        } />
    </List>
)

export const RoleEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <DisabledInput source="id" />
            <TextInput source="name" />
            <NumberInput source="permissions" />
            <RichTextInput source="desc" />
        </SimpleForm>
    </Edit>
);

export const RoleCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <NumberInput source="permissions" />
            <RichTextInput source="desc" />
        </SimpleForm>
    </Create>
);