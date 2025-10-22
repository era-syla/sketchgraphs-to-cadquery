import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04738, -0.02983).lineTo(-0.04738, -0.02983).lineTo(-0.04738, 0.02983).lineTo(0.04738, 0.02983).lineTo(0.04738, -0.02983).close()
solid=wp_sketch0.add(loop0).extrude(0.2145101539198842)
