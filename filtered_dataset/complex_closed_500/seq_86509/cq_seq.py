import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05872, 0.03927).lineTo(-0.03332, 0.03927).lineTo(0.06341, -0.01153).lineTo(0.06341, -0.02423).lineTo(-0.05872, -0.02423).lineTo(-0.05872, 0.03927).close()
solid=wp_sketch0.add(loop0).extrude(0.05495255997977884)
