import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0075, 0.01646).lineTo(0.0, 0.02396).lineTo(0.0075, 0.01646).lineTo(0.0075, -0.002).lineTo(-0.0075, -0.002).lineTo(-0.0075, 0.01646).close()
solid=wp_sketch0.add(loop0).extrude(0.04507640110887915)
