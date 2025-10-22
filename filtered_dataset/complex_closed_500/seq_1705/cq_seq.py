import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0335, -0.0195).lineTo(0.0505, -0.0195).lineTo(0.0505, -0.0281).lineTo(0.0335, -0.0281).lineTo(0.0335, -0.0195).close()
solid=wp_sketch0.add(loop0).extrude(-0.042834948622847674)
