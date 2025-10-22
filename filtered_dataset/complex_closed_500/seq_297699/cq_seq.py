import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.12297, 0.16499).lineTo(0.12703, 0.16499).lineTo(0.12703, -0.10501).lineTo(-0.12297, -0.10501).lineTo(-0.12297, 0.16499).close()
solid=wp_sketch0.add(loop0).extrude(0.46142773400367143)
