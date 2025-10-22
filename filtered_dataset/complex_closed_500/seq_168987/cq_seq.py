import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01641, 0.0).threePointArc((0.00018, 0.04152), (-0.01604, 0.0)).lineTo(-0.01022, -0.0).threePointArc((7e-05, 0.03547), (0.01037, -0.0)).lineTo(0.01641, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.13297909831329124)
