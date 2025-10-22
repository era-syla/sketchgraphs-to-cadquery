import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.11555, -0.03406).lineTo(-0.11555, -0.03406).lineTo(-0.11555, 0.03406).lineTo(0.11555, 0.03406).lineTo(0.11555, -0.03406).close()
solid=wp_sketch0.add(loop0).extrude(-0.06708284056720921)
