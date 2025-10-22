import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02069, -0.00062).lineTo(0.03614, -0.00062).lineTo(0.03614, -0.00312).lineTo(-0.02069, -0.00312).lineTo(-0.02069, -0.00062).close()
solid=wp_sketch0.add(loop0).extrude(-0.038233593814925554)
