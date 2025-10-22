import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.003, 0.01).lineTo(0.02044, 0.01).lineTo(0.02044, 0.002).lineTo(0.003, 0.002).lineTo(0.003, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(-0.02053113657858886)
