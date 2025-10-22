import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.7874, -0.41854).lineTo(0.635, -0.41854).lineTo(0.635, -0.26614).lineTo(0.7874, -0.26614).lineTo(0.7874, -0.41854).close()
solid=wp_sketch0.add(loop0).extrude(0.3936209787309309)
