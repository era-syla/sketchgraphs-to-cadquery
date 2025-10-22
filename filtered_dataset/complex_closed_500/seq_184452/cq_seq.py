import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.155, 0.21).lineTo(0.155, 0.21).lineTo(0.155, -0.21).lineTo(-0.155, -0.21).lineTo(-0.155, 0.21).close()
solid=wp_sketch0.add(loop0).extrude(0.8038739806917539)
