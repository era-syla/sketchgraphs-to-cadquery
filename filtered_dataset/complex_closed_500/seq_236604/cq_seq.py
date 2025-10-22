import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.23935, 0.35063).lineTo(-0.23935, 0.35063).lineTo(-0.23935, 0.075).lineTo(0.23935, 0.075).lineTo(0.23935, 0.35063).close()
solid=wp_sketch0.add(loop0).extrude(1.1506006534740112)
