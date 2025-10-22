import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00051, 0.01495).lineTo(-0.00051, 0.01495).lineTo(-0.00051, 0.01546).lineTo(0.00051, 0.01546).lineTo(0.00051, 0.01495).close()
solid=wp_sketch0.add(loop0).extrude(-0.0012085844400809163)
