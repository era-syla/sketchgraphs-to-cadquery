import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0175, 0.0).lineTo(-0.0175, -0.0).lineTo(-0.0175, 0.03).lineTo(0.0175, 0.03).lineTo(0.0175, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.07997048546848748)
