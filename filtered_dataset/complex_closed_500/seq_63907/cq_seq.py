import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.036, 0.671).lineTo(0.006, 0.671).lineTo(0.006, 0.703).lineTo(-0.036, 0.703).lineTo(-0.036, 0.671).close()
solid=wp_sketch0.add(loop0).extrude(-0.07483783883186208)
