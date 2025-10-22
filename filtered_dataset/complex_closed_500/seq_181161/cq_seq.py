import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.035).lineTo(0.018, 0.035).lineTo(0.03, -0.0).lineTo(0.0, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.07896788524939687)
