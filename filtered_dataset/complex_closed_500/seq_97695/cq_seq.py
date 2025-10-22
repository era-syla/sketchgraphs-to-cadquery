import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1231, -0.04475).lineTo(-0.12299, -0.04475).lineTo(-0.12299, 0.04473).lineTo(0.1231, 0.04473).lineTo(0.1231, -0.04475).close()
solid=wp_sketch0.add(loop0).extrude(0.3725576592476061)
