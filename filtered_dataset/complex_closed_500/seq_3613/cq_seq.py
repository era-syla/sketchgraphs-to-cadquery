import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01037, 0.02084).lineTo(0.0, 0.02512).lineTo(-0.01037, 0.02084).lineTo(0.01037, 0.02084).close()
solid=wp_sketch0.add(loop0).extrude(-0.028071014902023177)
