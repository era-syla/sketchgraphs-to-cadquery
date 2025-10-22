import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.089).lineTo(-0.051, 0.089).lineTo(-0.051, 0.086).lineTo(-0.0025, 0.086).lineTo(-0.0025, 0.0).lineTo(0.0, 0.0).lineTo(-0.0, 0.089).close()
solid=wp_sketch0.add(loop0).extrude(0.11312307091181066)
