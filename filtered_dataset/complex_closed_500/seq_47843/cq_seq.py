import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.135, 0.0).lineTo(-0.069, 0.0).lineTo(-0.03563, 0.028).lineTo(-0.0, 0.028).lineTo(-0.0, 0.06).lineTo(-0.04728, 0.06).lineTo(-0.08065, 0.032).lineTo(-0.135, 0.032).lineTo(-0.135, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.10904229689372022)
