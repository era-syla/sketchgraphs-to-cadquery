import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.40942, 0.18387).lineTo(0.40866, 0.16485).lineTo(0.39273, 0.16536).lineTo(0.39273, 0.18387).lineTo(0.40942, 0.18387).close()
solid=wp_sketch0.add(loop0).extrude(0.03112758406754655)
