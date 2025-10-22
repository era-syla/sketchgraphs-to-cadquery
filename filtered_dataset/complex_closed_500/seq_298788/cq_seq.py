import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07546, -0.07561).lineTo(0.07606, -0.07561).lineTo(0.07606, 0.07652).lineTo(-0.07546, 0.07652).lineTo(-0.07546, -0.07561).close()
solid=wp_sketch0.add(loop0).extrude(0.4161741878896217)
