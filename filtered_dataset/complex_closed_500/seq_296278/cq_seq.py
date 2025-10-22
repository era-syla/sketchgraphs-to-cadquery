import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04087, 0.00232).lineTo(-0.03587, 0.00232).lineTo(-0.03587, -0.00268).lineTo(-0.04087, -0.00268).lineTo(-0.04087, 0.00232).close()
solid=wp_sketch0.add(loop0).extrude(-0.003674234141308186)
