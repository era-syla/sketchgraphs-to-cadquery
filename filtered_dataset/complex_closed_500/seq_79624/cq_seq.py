import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.08459, -0.04875).lineTo(-0.08161, -0.04875).lineTo(-0.08161, 0.04538).lineTo(0.08459, 0.04538).lineTo(0.08459, -0.04875).close()
solid=wp_sketch0.add(loop0).extrude(-0.06994974996882038)
