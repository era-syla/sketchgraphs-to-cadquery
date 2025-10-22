import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05108, 0.03104).lineTo(0.03202, 0.03104).lineTo(0.03202, -0.01418).lineTo(-0.05108, -0.01418).lineTo(-0.05108, 0.03104).close()
solid=wp_sketch0.add(loop0).extrude(-0.11342819388445506)
