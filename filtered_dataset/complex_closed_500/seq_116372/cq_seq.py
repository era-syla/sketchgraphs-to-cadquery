import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.09282, -0.26416).lineTo(0.09627, -0.26416).lineTo(0.09627, -0.27966).lineTo(0.09282, -0.27966).lineTo(0.09282, -0.26416).close()
solid=wp_sketch0.add(loop0).extrude(0.025460217261349706)
