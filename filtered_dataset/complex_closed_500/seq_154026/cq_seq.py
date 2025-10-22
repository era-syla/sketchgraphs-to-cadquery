import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.031, -0.01061).lineTo(-0.016, -0.01061).lineTo(-0.016, -0.00889).lineTo(-0.031, -0.00889).lineTo(-0.031, -0.01061).close()
solid=wp_sketch0.add(loop0).extrude(-0.03739756285804653)
