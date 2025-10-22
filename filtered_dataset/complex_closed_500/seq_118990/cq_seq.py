import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01683, -0.00659).lineTo(-0.01683, -0.00659).lineTo(-0.01683, 0.00659).lineTo(0.01683, 0.00659).lineTo(0.01683, -0.00659).close()
solid=wp_sketch0.add(loop0).extrude(-0.018944229509312068)
