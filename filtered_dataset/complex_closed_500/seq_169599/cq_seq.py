import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0479, -0.0479).lineTo(-0.0479, -0.0479).lineTo(-0.0479, 0.0479).lineTo(0.0479, 0.0479).lineTo(0.0479, -0.0479).close()
solid=wp_sketch0.add(loop0).extrude(0.24035065262046415)
