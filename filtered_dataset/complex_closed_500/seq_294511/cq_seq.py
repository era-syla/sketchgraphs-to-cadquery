import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00651, 0.00299).lineTo(0.01612, 0.0265).lineTo(-0.00905, 0.02307).lineTo(0.00651, 0.00299).close()
solid=wp_sketch0.add(loop0).extrude(0.015259924499261552)
