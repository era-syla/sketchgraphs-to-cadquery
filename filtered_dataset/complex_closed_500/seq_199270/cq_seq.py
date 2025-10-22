import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.82762, 0.0).lineTo(-0.875, 0.0).lineTo(-0.875, -0.04738).lineTo(-0.04738, -0.875).lineTo(0.0, -0.875).lineTo(0.0, -0.82762).lineTo(-0.82762, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-2.115854069037127)
