import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01476, 0.00675).lineTo(0.0145, 0.00675).lineTo(0.0145, -0.00325).lineTo(0.0495, -0.00325).lineTo(0.0495, 0.00675).lineTo(0.04924, 0.00675).lineTo(0.01476, 0.00675).close()
solid=wp_sketch0.add(loop0).extrude(0.08746870902745522)
