import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-4.83655, 7.94549).lineTo(0.06345, 7.94549).lineTo(0.06345, -0.05451).lineTo(-4.83655, -0.05451).lineTo(-4.83655, 7.94549).close()
solid=wp_sketch0.add(loop0).extrude(-20.230262115120382)
