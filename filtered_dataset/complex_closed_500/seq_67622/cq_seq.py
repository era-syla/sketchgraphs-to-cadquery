import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-5.59176, 0.06096).lineTo(-3.9747, 0.06096).lineTo(-3.9747, 2.50095).lineTo(-5.59176, 2.50095).lineTo(-5.59176, 0.06096).close()
solid=wp_sketch0.add(loop0).extrude(-5.790671742624365)
