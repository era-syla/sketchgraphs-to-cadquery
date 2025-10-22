import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01473, -0.01937).lineTo(-0.01473, -0.03487).lineTo(0.01727, -0.03487).lineTo(0.01727, -0.0225).threePointArc((0.00138, -0.01983), (-0.01473, -0.01937)).close()
solid=wp_sketch0.add(loop0).extrude(0.044901970047637504)
