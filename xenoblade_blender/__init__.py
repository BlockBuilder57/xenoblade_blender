import bpy
from . import import_wimdo
from . import import_wismhd

bl_info = {
    "name": "Xenoblade Blender",
    "description": "Import Xenoblade models, maps, and animations",
    "author": "ScanMountGoat (SMG)",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "File > Import",
    "warning": "",
    "doc_url": "https://github.com/ScanMountGoat/xeno_blender/wiki",
    "tracker_url": "https://github.com/ScanMountGoat/xeno_blender/issues",
    "category": "Import-Export"
}


def menu_import_wimdo(self, context):
    text = "Xenoblade Model (.wimdo)"
    self.layout.operator(import_wimdo.ImportWimdo.bl_idname, text=text)


def menu_import_wismhd(self, context):
    text = "Xenoblade Map (.wismhd)"
    self.layout.operator(import_wismhd.ImportWismhd.bl_idname, text=text)


classes = [import_wimdo.ImportWimdo, import_wismhd.ImportWismhd]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_import_wimdo)
    bpy.types.TOPBAR_MT_file_import.append(menu_import_wismhd)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_file_import.remove(menu_import_wimdo)
    bpy.types.TOPBAR_MT_file_import.remove(menu_import_wismhd)


if __name__ == "__main__":
    register()