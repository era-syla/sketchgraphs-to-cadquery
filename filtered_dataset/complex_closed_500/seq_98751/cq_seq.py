import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.104, 0.104).lineTo(-0.104, 0.104).lineTo(-0.104, -0.104).lineTo(0.104, -0.104).lineTo(0.104, 0.104).close()
solid=wp_sketch0.add(loop0).extrude(0.5454087289650784)
