import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0614, 0.0).lineTo(0.0614, 0.05468).lineTo(0.0, 0.05468).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.04893926771323958)
