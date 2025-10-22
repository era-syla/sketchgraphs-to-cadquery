import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.013, 0.0862).lineTo(0.129, 0.0862).lineTo(0.129, 0.0172).lineTo(0.013, 0.0174).lineTo(0.013, 0.0862).close()
solid=wp_sketch0.add(loop0).extrude(0.2438920920776473)
