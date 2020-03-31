from core.iDDS.constants import RequestStatus, RequestType, TransformType, \
    TransformStatus, CollectionStatus, ProcessingStatus, ContentStatus

class SubstitleValue:

    substitleMap = {
        'requests':{'status':{}, 'request_type':{}},
        'transforms':{'transform_id_fk__status':{}, 'transform_id_fk__transform_type':{}},
        'collections':{'status':{}},
        'processings':{'status':{}},
        'сontents':{'status':{}}
    }


    def getKlassName(self, objName, field):
        klassname = None
        if objName == 'requests':
            if field == 'status':
                klassname = RequestStatus
            elif field == 'request_type':
                klassname = RequestType

        elif objName == 'transforms':
            if field == 'transform_id_fk__status':
                klassname = TransformStatus
            elif field == 'transform_id_fk__transform_type':
                klassname = TransformType

        elif objName == 'collections':
            if field == 'status':
                klassname = CollectionStatus

        elif objName == 'processings':
            if field == 'status':
                klassname = ProcessingStatus

        elif objName == 'сontents':
            if field == 'status':
                klassname = ContentStatus
        return klassname


    def __init__(self):
        for objName, fields in self.substitleMap.items():
            for field in fields.keys():
                self.substitleMap[objName][field] =  self.substitleValue(objName, field)


    def substitleValue(self, objName, field):
        klass = self.getKlassName(objName, field)
        enumMembers = klass.__members__
        enumMap = {}
        for member in enumMembers:
            enumMap[enumMembers[member].value] = enumMembers[member].name
        return enumMap


    def replace(self, objName, objList):
        for objects in objList:
            fieldsToSub = set(objects.keys()) & set(self.substitleMap[objName])
            for field in fieldsToSub:
                valueToSubTitle = objects[field]
                objects[field] = self.substitleMap[objName][field][valueToSubTitle]