/**
 * 
 * @authors Shanming (shanming0428@163.com)
 * @date    2019-07-12 23:47:08
 * @version $Id$
 */

import React from 'react';
import {
    List,
    Datagrid,
    TextField,
    ReferenceField,
    EditButton,
    Edit,
    SimpleForm,
    DisabledInput,
    ReferenceInput,
    SelectInput,
    TextInput,
    LongTextInput,
    Create,
    Filter,
    SimpleList,
    Responsive,
    DateTimeInput,
    DateField
}
from 'react-admin';
import RichTextInput from 'ra-input-rich-text';

const RecordTitle = ({record}) =>
{
    return <span>Record: {record ? `"${record.title}"` : ''}</span>;
};

const RecordFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="q" alwaysOn />
        <ReferenceInput label="User" source="userId" reference="users" allowEmpty>
            <SelectInput optionText="name" />
        </ReferenceInput>
    </Filter>
);


export const RecordList = (props) => (
    <List {...props}>
        <Responsive
            small={
                <SimpleList
                    primaryText={record => record.user_name}
                    secondaryText={record => record.course_name}
                    tertiaryText={record => new Date(record.logged).toLocaleDateString()}
                />
            }
            medium={
                <Datagrid>
                    <TextField source="id" />
                    <ReferenceField source="user_id" reference="users">
                        <TextField source="name" />
                    </ReferenceField>
                    <ReferenceField source="course_id" reference="courses">
                        <TextField source="name" />
                    </ReferenceField>
                    <DateField source="logged" />
                    <TextField source="comment" />
                    <EditButton />
                </Datagrid>
            }
        />
    </List>
);

export const RecordEdit = props => (
    <Edit title={<RecordTitle/>} {...props}>
        <SimpleForm>
           <DisabledInput source="id" />
            <ReferenceInput source="user_id" reference="users">
               <SelectInput optionText="name" />
            </ReferenceInput>
            <ReferenceInput source="course_id" reference="courses">
               <SelectInput optionText="name" />
            </ReferenceInput>
            <RichTextInput source="comment" />
           <DateTimeInput source="logged" />
        </SimpleForm>
    </Edit>
);

export const RecordCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <ReferenceInput source="user_id" reference="users">
                <SelectInput optionText="name" />
            </ReferenceInput>
            <ReferenceInput source="course_id" reference="courses">
                <SelectInput optionText="name" />
            </ReferenceInput>
            <RichTextInput source="comment" />
            <DateTimeInput source="logged" defaultValue={new Date()} />
        </SimpleForm>
    </Create>
);