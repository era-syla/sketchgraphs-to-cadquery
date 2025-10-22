import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01588, -0.05715).lineTo(-0.04608, -0.05715).lineTo(-0.04608, 0.05715).lineTo(0.01588, 0.05715).lineTo(0.01588, -0.05715).close()
solid=wp_sketch0.add(loop0).extrude(-0.15718669038665783)
