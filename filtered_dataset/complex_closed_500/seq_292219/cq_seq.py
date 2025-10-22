import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00457, -0.0053).lineTo(-0.00457, -0.0053).lineTo(-0.00457, 0.0053).lineTo(0.00457, 0.0053).lineTo(0.00457, -0.0053).close()
solid=wp_sketch0.add(loop0).extrude(-0.012845706243134986)
