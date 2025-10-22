import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.06671, -0.02986).lineTo(0.036, -0.02986).lineTo(0.036, 0.05086).lineTo(0.06671, 0.05086).lineTo(0.06671, -0.02986).close()
solid=wp_sketch0.add(loop0).extrude(-0.08383773439842263)
