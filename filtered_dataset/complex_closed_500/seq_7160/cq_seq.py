import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05678, -0.02512).threePointArc((0.06341, -0.01849), (0.05678, -0.01186)).lineTo(-0.06326, -0.01186).threePointArc((-0.0591, -0.01849), (-0.06326, -0.02512)).lineTo(0.05678, -0.02512).close()
solid=wp_sketch0.add(loop0).extrude(0.3547922213622449)
