import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01892, 0.01287).lineTo(0.00612, 0.01287).lineTo(0.00612, 0.02232).lineTo(0.01892, 0.02232).lineTo(0.01892, 0.01287).close()
solid=wp_sketch0.add(loop0).extrude(-0.01895200821099387)
