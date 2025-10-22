import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.02222).lineTo(-0.04445, 0.02222).lineTo(-0.04445, 0.06667).lineTo(-0.0, 0.06667).lineTo(0.0, 0.02222).close()
solid=wp_sketch0.add(loop0).extrude(0.09933063005925365)
