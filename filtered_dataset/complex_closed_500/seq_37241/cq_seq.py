import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.31, -0.315).lineTo(-0.31, -0.315).lineTo(-0.31, 0.315).lineTo(0.31, 0.315).lineTo(0.31, -0.315).close()
solid=wp_sketch0.add(loop0).extrude(-0.4895352124891758)
