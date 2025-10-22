import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.35, 0.1).lineTo(-0.35, 0.1).lineTo(-0.35, -0.1).lineTo(0.35, -0.1).lineTo(0.35, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(2.066575974981187)
