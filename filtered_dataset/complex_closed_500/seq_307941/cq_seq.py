import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06632, -0.05526).lineTo(0.06879, -0.01623).lineTo(0.08668, 0.03799).lineTo(0.07227, 0.0389).lineTo(0.05569, -0.0559).lineTo(0.06632, -0.05526).close()
solid=wp_sketch0.add(loop0).extrude(-0.23789780404682417)
